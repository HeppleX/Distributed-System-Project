<template>
  <div class="login">
    <div class="container-login100">
      <div class="wrap-login100">
        <!-- <div class="login100-pic js-tilt" data-tilt>
          <img src="@/assets/logo.png" alt="IMG">
        </div> -->

        <form class="login100-form validate-form">
          <span class="login100-form-title">
            Login
          </span>

          <a-form class="loginForm" :model="formState" name="basic" :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }" autocomplete="off"
            @finish="onFinish" @finishFailed="onFinishFailed">
            <a-form-item label="student_id" name="student_id"
              :rules="[{ required: true, message: 'Please input your student_id!' }]">
              <a-input v-model:value="formState.student_id" />
            </a-form-item>

            <a-form-item label="Password" name="password"
              :rules="[{ required: true, message: 'Please input your password!' }]">
              <a-input-password v-model:value="formState.password" />
            </a-form-item>

            <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
              <a-button type="primary" html-type="submit">Log In</a-button>
            </a-form-item>
          </a-form>

          <div class="text-center p-t-12">
            <a class="txt2" href="javascript:">
              Forget password?
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { postAPI } from '../../utils/api';
import { reactive } from 'vue';
import { message } from 'ant-design-vue';
import router from '@/router';
import instance from '@/utils/request'
import Cookie from 'js-cookie';
const [messageApi, contextHolder] = message.useMessage();
const formState = reactive({
  student_id: '',
  password: '',
  remember: true,
});
const onFinish = values => {
  console.log('Success:', values);
  postAPI('/login', {
          "password": formState.password,
          "student_id": formState.student_id
      }).then(res => {
        if(res.status && res.status == 200) {
          var token = res.data.access_token;
          Cookie.set('token', token);
          var student_name = res.data.student_name;
          instance.defaults.headers.common['Authorization'] = 'Bearer ' + token;
          Cookie.set('student_name', student_name);
          router.push('/home');
        }else {
            message.info('Wrong account or password!');
        }
      }).catch(err => {
          message.info('Wrong account or password!');
      })
};
const onFinishFailed = errorInfo => {
  console.log('Failed:', errorInfo);
  messageApi.info('Empty account or password!');
};
</script>

<style scoped>
@import url('./index.css');
</style>