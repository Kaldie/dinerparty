import { UserService } from '@/client/service/users'
import { account } from '../store/account'

// call this function when a valid token is required
// the first param should be the function
// followed by its arguments
// the after the arguments, give a callback on succes and failure
export const retryAfterTokenRefresh = (...args) => {
  const action = args[0]
  let currentArgumentNumber = 1
  const parameters = []
  while (typeof args[currentArgumentNumber] !== "function" && currentArgumentNumber < args.length) {
    parameters.push(args[currentArgumentNumber])
    ++currentArgumentNumber
  }

  // eslint-disable-next-line no-unused-vars
  let succes = (result) => result
  if (args[currentArgumentNumber]) {
    succes = args[currentArgumentNumber]
    ++currentArgumentNumber
  }

  // eslint-disable-next-line no-unused-vars
  let failure = (error) => error
  if (args[currentArgumentNumber]) {
    failure = args[currentArgumentNumber]
    ++currentArgumentNumber
  }

  return action(...parameters)
  .then(
    result => succes(result),
    error => {
      if (error.response.data && error.response.data.msg) {
        if ("Token has expired" === error.response.data.msg) {
          UserService.refreshToken()
          .then(
            result => {
              account.mutations.refreshSucces(account.state, result.data.access_token)
              return action(...parameters).then(
                result => succes(result),
                error => failure(error)
              )
            }
          )
        } else {
          failure(error)
        }
      } else {
        failure(error)
      }
    }
  )
}