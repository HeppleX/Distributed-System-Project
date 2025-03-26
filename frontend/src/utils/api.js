import http from './http'

// get请求
export function getAPI(url, params){
    return http.get(url, params)
}
// post请求
export function postAPI(url, params){
    return http.post(url, params)
}
// put 请求
export function putSomeAPI(url, params){
    return http.put(url, params)
}
// delete 请求
export function deleteListAPI(url, params){
    return http.delete(url, params)
}