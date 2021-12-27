import { JoinRequest, User, Game } from './dispatcher_pb'
import { DispatcherPromiseClient } from './dispatcher_grpc_web_pb'

export function createUser(uuid, name) {
    let res = new User();
    res.setUuid(uuid);
    res.setName(name);
    return res;
}


export function createGame({owner, state, address, port}) {
    let res = new Game();
    let user = createUser(owner.uuid, owner.name);
    res.setOwner(user);
    res.setState(state);
    res.setAddress(address);
    res.setPort(port);
    return res;
}

export class Client {
    constructor(user) {
        // user - текущий пользователь
        this.connection = new DispatcherPromiseClient("http://172.16.10.38:8080", null, null);
        this.user = user;
        this.games = [];
        this.getGameList();
        this.getGameListIntervalID = setInterval(() => {
            this.getGameList();
        }, 5000);
    }

    async joinPlayer(game) {
        // Подключение текущего пользователя "user" к выбранной игре "game" как игрок
        // Возвращает ответ сервера
        let request = new JoinRequest();
        request.setUser(this.user);
        request.setGame(game);
        try {
            let status = await this.connection.joinPlayer(request, {});
            return status.toObject();
        } catch(err) {
            console.log('joinPlayer err', err);
        }
    }

    async joinVisitor(game) {
        // Подключение пользователя "user" к выбранной игре "game" как зритель
        // Возвращает ответ сервера
        let request = new JoinRequest();
        request.setUser(this.user);
        request.setGame(game);
        try {
            let status = await this.connection.joinVisitor(request, {});
            return status.toObject();
        } catch(err) {
            console.log('joinVistion err', err);
        }
    }

    async createGame() {
        // Создание комнаты (игры) под текущим пользователем
        // Возвращает созданную игру
        try {
            let game = await this.connection.createGame(this.user, {});
            return game.toObject();
        } catch(err) {
            console.log('createGame err', err);
        }
    }

    async closeGame(game) {
        // Закрывает игру "game"
        try {
            let status = await this.connection.closeGame(game, {});
            return status.toObject();
        } catch(err) {
            console.log('closeGame err', err);
        }
    }

    getGameList() {
        // Получает список игр
        this.cnt++;
        this.games.length = 0; // очищение старого списка
        let stream = this.connection.getGameList(this.user, {});
        stream.on('data', (response) => {
            this.games.push(response.toObject());
        });
        stream.on('error', (err) => {
            console.log(`Unexpected stream error: code = ${err.code}` +
                `, message = "${err.message}"`);
        });
        console.log('New game list has been received!');
        return this.games;
    }

}