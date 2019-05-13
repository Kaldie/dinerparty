import { AuthHeader, CrossOriginHeader, RefreshHeader } from '@/client/utilities'
import axios from 'axios'
import Settings from '@/client/settings.js'

const login = (userName, password) => {  

  const config = {
    headers:  CrossOriginHeader,
    }
  const data = {
    username:userName,
    password}

  return axios.post(`http://${Settings.server}:${Settings.port}/login`, data ,config)
    .then(result => result.data)
}

const logout = () => {  

  let config ={
    headers: Object.assign(AuthHeader, CrossOriginHeader),
  }
  
  return axios.post(`http://${Settings.server}:${Settings.port}/logout/refresh`, config)
  .then(() => {
    return axios.post(`http://${Settings.server}:${Settings.port}/logout/access`, config)
    })
}

const register = (user) => {
  let config ={
    headers: CrossOriginHeader,
    data: user
  }
  return axios.post(`http://${Settings.server}:${Settings.port}/registration`, user, config)
  
}

const refreshToken = () => {

  const config = {
    headers: Object.assign(RefreshHeader, CrossOriginHeader),
    }

  return axios.post(`http://${Settings.server}:${Settings.port}/token/refresh`, config)
}

const getALl = () => {

  let config = {
    headers: Object.assign(AuthHeader, CrossOriginHeader),
  }

  return axios.get(`http://${Settings.server}:${Settings.port}/users`, config)
}



export const UserService = {
  login,
  logout,
  register,
  getALl,
  refreshToken
}