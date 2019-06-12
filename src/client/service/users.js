import { AuthHeader, CrossOriginHeader, RefreshHeader } from '@/client/utilities'
import axios from 'axios'
import Settings from '@/client/settings.js'
import objectToFormData from 'object-to-formdata'

axios.defaults.baseURL = `http://${Settings.server}:${Settings.port}/`

const login = (username, password) => {  
  const config = {
    headers:  CrossOriginHeader,
  }

  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  return axios.post('login', formData, config )
}

const logout = () => {  

  const refreshConfig = {
    headers: Object.assign(RefreshHeader(), CrossOriginHeader)
  }

  let config ={
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }
 
  return axios.post(`logout/refresh`,{}, refreshConfig)
  .then(() => {
    return axios.post(`logout/access`,{}, config)
    })
}

const register = (user) => {
  let config = {
    headers: CrossOriginHeader
  }
  return axios.post(`registration`, objectToFormData(user), config)
}

const refreshToken = () => {

  const config = {
    headers: Object.assign(RefreshHeader(), CrossOriginHeader),
    }

  return axios.post(`token/refresh`, {}, config)
}

const getALl = () => {

  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }

  return axios.get(`users`, config)
}

const update = (user) => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }
  return axios.patch(`user`, objectToFormData(user), config)
}

const get = () => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }
  return axios.get(`user`,config)
}

const resetPassword = (passwordObject) => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader)
  }
  return axios.post(`user/password`, objectToFormData(passwordObject), config)
}

const getUser = (id) => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader)
  }
  return axios.post(`user/${id}`, config)
}



export const UserService = {
  login,
  logout,
  update,
  get,
  register,
  getALl,
  getUser,
  refreshToken,
  resetPassword
}