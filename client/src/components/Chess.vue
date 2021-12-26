<template>
  <div id="app">
  <chessboard :fen="currentFen"  @onMove="showInfo" />
    <div>
    {{this.positionInfo}}
    </div>
  </div>
</template>

<script>
import {chessboard} from 'vue-chessboard'
import 'vue-chessboard/dist/vue-chessboard.css'


export default {
  name: 'chessboard2',
  components:
  {chessboard},
  data () {
    return {
      currentTurn: 'white',
      currentFen: '',
      positionInfo: null,
      connection: null,
      currentOrientation: "white",
      isWaiting:false,
      isViewer: false
    }
  },
  methods: {
    showInfo(data) {
        this.$children[0].board.set({orientation:this.currentOrientation,viewOnly:this.isWaiting})
        if (data.fen===this.currentFen)
            return
        this.gameData=data
        try{
            var myObj = new Object();
            myObj.fen = data.fen;
            myObj.isViewer = this.isViewer;
            myObj.messageType = "Standart";
            this.sendMessage(JSON.stringify(myObj));
        }
        catch(err)
        {
            console.log("ERROR")
        }

      },

    sendMessage(message) {
        //console.log(this.connection);
        try {
            this.connection.send(message);

        }
        catch (err) {
            console.log("err")
        }
      

    },
    connect() {
        console.log("Starting connection to WebSocket Server")
        this.connection = new WebSocket("ws://localhost:5001")
        let vm = this


        this.connection.onmessage = function (event) {
            try {
                var dic = JSON.parse(event.data);

                vm.currentOrientation = dic.orientation;
                vm.isViewer = dic.status === 'true'
                vm.isWaiting = dic.status === 'true'
                vm.$children[0].board.set({ viewOnly: true });
                console.log(vm.$children[0].game.turn()[0]);
                console.log(vm.currentOrientation[0]);
            }
            catch (e) {

                vm.$children[0].game.load(event.data)
                if (vm.isViewer !== true) {
                    if (vm.$children[0].game.turn()[0] !== vm.currentOrientation[0]) {

                        vm.$children[0].board.set({ viewOnly: true })
                        vm.isWaiting = true
                    }
                    else {
                        vm.$children[0].board.set({ viewOnly: false })
                        vm.isWaiting = false
                    }
                }
            }


            vm.currentFen = event.data;
            vm.$children[0].board.set({ orientation: vm.currentOrientation })
        }

        this.connection.onopen = function (event) {
            console.log(event)
            console.log("Successfully connected to the echo websocket server...")
            vm.$children[0].board.set({ orientation: vm.currentOrientation })
            setTimeout(() => {
                var myObj = new Object(); myObj.messageType = "Init"; myObj.user_id = localStorage.getItem('user_id');
                vm.sendMessage(JSON.stringify(myObj))
            }, 10);
        }

        this.connection.onclose = function (event) {
            console.log(event)
            if (!event.wasClean) {
                    alert("Server is down... Reconnecting...")
                    setTimeout(function () {
                        vm.connect();
                    }, 5000);


            }
        }



      },
    async  isOnline() {
        try {
            await fetch("https://google.com");
            return true;
        }
        catch (err) {
            console.log(err)
        }

        return false;
      },
    uuid() {
        var uuidValue = "", k, randomValue;
        for (k = 0; k < 32; k++) {
            randomValue = Math.random() * 16 | 0;

            if (k == 8 || k == 12 || k == 16 || k == 20) {
                uuidValue += "-"
            }
            uuidValue += (k == 12 ? 4 : (k == 16 ? (randomValue & 3 | 8) : randomValue)).toString(16);
        }
        return uuidValue;
    }


  },
  created: function()
  {
      this.connect()
      if (localStorage.getItem("user_id") === null)
      { localStorage.setItem("user_id", this.uuid()) }
      
      //console.log(this.$cookie.get('user_id'))

  },
  mounted ()
  {

        this.$children[0].board.set({viewOnly:false})

  }
}


</script>

