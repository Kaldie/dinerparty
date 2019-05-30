import { AuthHeader, CrossOriginHeader, RefreshHeader } from '@/client/utilities'
import axios from 'axios'
import Settings from '@/client/settings.js'

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
  const formData = new FormData();
  formData.append("username", user.username)
  formData.append("password", user.password)
  formData.append("email", user.email)
  formData.append("address", user.address)
  formData.append("city", user.city)
  return axios.post(`registration`, formData, config)
  
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
  const formData = new FormData();
  formData.append("username", user.username)
  formData.append("email", user.email)
  formData.append("address", user.address)
  formData.append("city", user.city)

  return axios.patch(`user`, formData,config)
}

const get = () => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }
  return axios.get(`user`,config)
}

const resetPassword = (passwordObject) => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }
    const formData = new FormData();
    formData.append("previousPassword", passwordObject.previousPassword)
    formData.append("newPassword", passwordObject.newPassword)

    return axios.post(`user/password`, formData, config)
}



export const UserService = {
  login,
  logout,
  update,
  get,
  register,
  getALl,
  refreshToken,
  resetPassword
}