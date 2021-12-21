<!--
Inline countdown timer with 'mm:ss.000' format.
Starts on prop 'run' === true.
Stops on  prop 'run' === false or when runs out of time.
Emits events on 'start', 'stop', and 'end' (when out of time).
-->

<template>
  <span>{{zeroPadding(countMinutes,2)}}:{{zeroPadding( countSeconds.toFixed(3),6 )}}</span>
</template>

<script>
// Timer refresh period
// ATTENTION!!! If the value is less than 10, browser uses 10, TIMING BREAKS!!!
// 11 but not 10 - to make last digit not frozen
const PERIOD = 11;

export default {
  name: 'Countdown',

  props: {
    minutes: { type: Number, default: 0 },
    seconds: { type: Number, default: 0 },
    run: { type: Boolean, default: false },
  },

  data() {
    return {
      countMinutes: this.minutes,
      countSeconds: this.seconds,
      timerID: null,
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
      this.timerID = setInterval(this.decrementTime, PERIOD);
    },

    stop() {
      clearInterval(this.timerID);
      this.$emit('stop');
    },

    decrementTime() {
      if (this.countMinutes === 0 && this.countSeconds < PERIOD / 1000) {
        this.countSeconds = 0; // cut the tail less than PERIOD
        this.stop();
        this.$emit('end');
        return;
      }
      if (this.countSeconds < PERIOD / 1000) {
        this.countMinutes -= 1;
        this.countSeconds += 60 - (PERIOD / 1000);
      } else {
        this.countSeconds -= PERIOD / 1000;
      }
    },

    zeroPadding(number, width) {
      return ('0'.repeat(width) + String(number)).slice(-width);
    }

  }
};
</script>
