import {authHeader} from '@/client/utilities/authHeader'
import axios from 'axios'
import Settings from '@/client/settings.js'

const login = (userName, password) => {  

  let config = {
    headers: {
      "Access-Control-Allow-Origin": "127.0.0.1:5000",
    },
    params: {
      userName,
      password}
    }

  return axios.get(`http://${Settings.server}:${Settings.port}/user/`, config)
  .catch((error) => {
    console.warn(error)
  }).then((response) => {
    this.parties = response.data
    return response.data
  })
}


export const userService = {
  login,
  logout,
  register,
  getAll,
  getById,
  update,
  delete: _delete
}