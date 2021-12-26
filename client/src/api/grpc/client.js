import { User, Game, JoinRequest } from './dispatcher_pb'
import { DispatcherClient } from './dispatcher_grpc_web_pb'

export default class {
    constructor() {
        this.connection = new DispatcherClient("http://localhost:8080", null, null);
    }

    joinGame() {
        let user = new User("some_uuid", "some_name");
        let game = new Game(
            user,
            1,
            "some_address",
            "some_port"
        );
        let join_request = new JoinRequest(user, game);
        this.connection.joinPlayer(
            join_request,
            {},
            (err, response) => {
                console.log(err);
                console.log(response);
            }
        );
    }
}