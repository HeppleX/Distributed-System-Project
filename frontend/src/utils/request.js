import axios from "axios";
import Cookie from 'js-cookie';
const baseURL= process.env.NODE_ENV === 'development'? '/api' : 'http://127.0.0.1:5000';
const instance = axios.create({
  baseURL,
  timeout: 5000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Authorization': 'Bearer ' + Cookie.get('token')
  }
});
instance.interceptors.response.use(function (response) {
  return response;
}, function (error) {
  return error.response
}, error => {
  if (error && error.response) {
    switch (error.response.status) {
      default:
        error.message = `Connection Error${error.response.status}`
    }
  } else {
    // 超时处理
    if (JSON.stringify(error).includes('timeout')) {
      Message.error('The server response timed out, please refresh the current page')
    }
    error.message = 'Failed to connect to the server'
  }

  Message.error(error.message)

  return Promise.reject(error);
});
export default instance