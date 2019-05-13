import { store }  from '@/client/store'

export function AuthHeader() {
  // return authorization header with jwt token
  let user = store.account.state.user
  console.warn("user", user)
  if (user && user.token) {
      return { 'Authorization': 'Bearer ' + user.token };
  } else {
      return {};
  }
}

export function RefreshHeader() {
  // return authorization header with jwt token
  let user = store.account.state.user;

  if (user && user.refresh_token) {
      return { 'Authorization': 'Bearer ' + user.refresh_token };
  } else {
      return {};
  }
}