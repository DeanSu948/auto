// appfront/src/api/api.js

// 导入之前配置好的 axios 实例
import axiosInstance from './index'

// 将导入的 axios 实例赋值给 axios 变量
const axios = axiosInstance

// 定义获取图书列表的 HTTP GET 请求方法
export const getRuns = () => {return axios.get(`http://localhost:8000/api/FlashInfo/`)}

// 定义添加图书的 HTTP POST 请求方法
export const postRun = (soft_ver, hil_id) => {return axios.post(`http://localhost:8000/api/FlashInfo/`, {'soft_ver': soft_ver, 'hil_id': hil_id})}
