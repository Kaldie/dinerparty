import { createOvermind } from 'overmind';
import { createPlugin } from 'overmind-vue';
import * as state from './state'

const overmind = createOvermind({
  state,
  actions: {
    onClick() {
      // tslint:disable-next-line:no-console
      console.warn('here');
    },
  },
});

export const OvermindPlugin = createPlugin(overmind);
