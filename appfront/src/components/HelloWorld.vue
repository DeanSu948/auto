<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <!-- show books list -->
    <ul>
      <li v-for="(run, index) in runs" :key="index" style="display:block">
        {{index}}-{{run.soft_ver}}-{{run.hil_id}}
      </li>
    </ul>

    <!-- form to add a flash_info -->
    <form action="">
      输入Soft_Ver：<input type="text" placeholder="soft_ver" v-model="inputRun.soft_ver"><br>
      输入Hil_ID：<input type="text" placeholder="hil_id" v-model="inputRun.hil_id"><br>
    </form>
    <button type="submit" @click="runSubmit()">submit</button>
  </div>
</template>

<script>
import {getRuns, postRun} from '../api/api.js'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      // books list data
      runs: [
        {soft_ver: 'test1', hil_id: 't1'},
        {soft_ver: 'test2', hil_id: 't2'}
      ],
      // book data in the form
      inputRun: {
        "soft_ver": "",
        "hil_id": "",
      }
    }
  },
  methods: {
    loadRuns() {
      getRuns().then(response => {
        this.runs = response.data
      })
    }, // load books list when visit the page
    runSubmit () {
      postRun(this.inputRun.soft_ver, this.inputRun.hil_id).then(response => {
        console.log(response)
        this.loadRuns()
      })
    } // add a book to backend when click the button
  },
  created: function () {
    this.loadRuns()
  }
}
</script>
