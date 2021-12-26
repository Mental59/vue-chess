import { JoinRequest, User, Game } from './dispatcher_pb'
import { DispatcherClient } from './dispatcher_grpc_web_pb'

export function createUser(uuid, name) {
    let res = new User();
    res.setUuid(uuid);
    res.setName(name);
    return res;
}

export function createGame(owner, state, address, port) {
    let res = new Game();
    res.setOwner(owner);
    res.setState(state);
    res.setAddress(address);
    res.setPort(port);
    return res;
}

export class Client {
    constructor(user) {
        // user - текущий пользователь
        this.connection = new DispatcherClient("http://localhost:8080", null, null);
        this.user = user;
    }

    joinPlayer(game) {
        // Подключение текущего пользователя "user" к выбранной игре "game" как игрок
        // Возвращает ответ сервера
        let status = null;
        let request = new JoinRequest();
        request.setUser(this.user);
        request.setGame(game);
        this.connection.joinPlayer(
            request,
            {},
            (err, response) => {
                console.log(err);
                console.log(response);
                if (!err) {
                    status = response.toObject();
                }       
            }
        );
        return status;
    }

    joinVisitor(game) {
        // Подключение пользователя "user" к выбранной игре "game" как зритель
        // Возвращает ответ сервера
        let status = null;
        let request = new JoinRequest();
        request.setUser(this.user);
        request.setGame(game);
        this.connection.joinVisitor(
            request,
            {},
            (err, response) => {
                console.log(err);
                console.log(response);
                if (!err) {
                    status = response.toObject();
                }
            }
        );
        return status;
    }

    createGame() {
        // Создание комнаты (игры) под текущим пользователем
        // Возвращает созданную игру
        let game = null;
        this.connection.createGame(
            this.user,
            {},
            (err, response) => {
                console.log(err);
                console.log(response);
                if (!err) {
                    game = response.toObject();
                };
            }
        );
        return game;
    }

    closeGame(game) {
        // Закрывает игру "game"
        let status = null;
        this.connection.closeGame(
            game,
            {},
            (err, response) => {
                console.log(err);
                console.log(response);
                if (!err) {
                    status = response.toObject();
                }
            }
        )
        return status;
    }

    getGameList() {
        // Получает список игр
        let games = [];

        var stream = this.connection.getGameList(this.user, {});
        stream.on('data', (response) => {
            games.push(response.toObject());
        });
        stream.on('error', (err) => {
            console.log(`Unexpected stream error: code = ${err.code}` +
                `, message = "${err.message}"`);
        });

        return games;
    }

}