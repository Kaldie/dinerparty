import { store }  from '@/client/store'


export function AuthHeader() {
  // return authorization header with jwt token
  if (store.state.account.user && store.state.account.user.access_token) {
      return { 'Authorization': 'Bearer ' + store.state.account.user.access_token };
  } 
  return {};
}

export function RefreshHeader() {
  if (store.state.account.user && store.state.account.user.refresh_token) {
      return { 'Authorization': 'Bearer ' + store.state.account.user.refresh_token };
  } 
  return {};
}