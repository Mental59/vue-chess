<!--
Countdown timer clock with Stop button.
Uses Countdown component, wraps it with design and controls.
Makes Countdown start on prop 'run' === true.
Makes Countdown stop on  prop 'run' === false or when Stop button is pressed.
Propagates Countdown's 'start', 'stop', and 'end' events.
Makes clock face red when out of time.
-->

<template>

  <div class="stop-clock">

    <div class="stop-clock__face" :class="{'stop-clock__face_countdown-ended': isEnded, 'active-clock': run }">
      <span>
        {{ zeroPadding(countMinutes, 2) }}:{{ zeroPadding(countSeconds, 2) }}
      </span>
    </div>

  </div>

</template>


<script>
export default {
  name: 'StopClock',
  props: {
    minutes: { type: Number, default: 0 },
    seconds: { type: Number, default: 0 },
    run: { type: Boolean, default: false },
    period: {type: Number, default: 1000},
  },
  data() {
    return {
      countMinutes: this.minutes,
      countSeconds: this.seconds,
      timerID: null,
      isEnded: false,
    }
  },
  watch: {
    run() {
      this.decideStartOrStop();
    }
  },
  mounted() {
    this.decideStartOrStop();
  },
  methods: {
    decideStartOrStop() {
      if (this.run) {
        this.start();
      } else {
        this.stop();
      }
    },
    start() {
      this.$emit('start');
      this.timerID = setInterval(this.decrementTime, this.period);
    },
    stop() {
      clearInterval(this.timerID);
      this.$emit('stop');
    },
    decrementTime() {
      if (this.countMinutes === 0 && this.countSeconds < this.period / 1000) {
        this.countSeconds = 0; // cut the tail less than this.period
        this.stop();
        this.isEnded = true;
        this.$emit('end');
        return;
      }
      
      if (this.countSeconds < this.period / 1000) {
        this.countMinutes -= 1;
        this.countSeconds += 60 - (this.period / 1000);
      } else {
        this.countSeconds -= this.period / 1000;
      }
    },
    
    increaseTime(seconds) {
      const countedSeconds = this.countSeconds + seconds;
      if (countedSeconds > 60) {
        this.countMinutes += Math.floor(countedSeconds / 60);
        this.countSeconds = countedSeconds % 60;
      } else {
        this.countSeconds = countedSeconds;
      }
    },

    setTime(seconds) {
      this.countSeconds = seconds % 60;
      this.countMinutes = Math.floor(seconds / 60);
    },

    zeroPadding(number, width) {
      return ('0'.repeat(width) + String(number)).slice(-width);
    }
  }
};
</script>


<style>
.stop-clock {
  text-align: center;
}
.stop-clock__face {
  font-family: monospace;
  font-size: 50px;
  color: #bababa;
  padding: 10px;
  background-color: #262421;
  width: 300px;
}
.stop-clock__face_countdown-ended {
  background-color: #D45A18;
  color: white;
}
.active-clock {
    background-color: #384722;
}
</style>