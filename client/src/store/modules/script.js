import Vue from 'vue';

import { makeURL } from '@/js/utils';

export default {
  state: {
    currentRevision: null,
    revisions: [],
    script: {},
  },
  mutations: {
    SET_REVISIONS(state, revisions) {
      state.revisions = revisions;
    },
    SET_CURRENT_REVISION(state, currentRevision) {
      state.currentRevision = currentRevision;
    },
    SET_SCRIPT_PAGE(state, { pageNumber, page }) {
      Vue.set(state.script, pageNumber, page);
    },
  },
  actions: {
    async GET_SCRIPT_REVISIONS(context) {
      const response = await fetch(`${makeURL('/api/v1/show/script/revisions')}`);
      if (response.ok) {
        const revisions = await response.json();
        context.commit('SET_REVISIONS', revisions.revisions);
        context.commit('SET_CURRENT_REVISION', revisions.current_revision);
      } else {
        console.error('Unable to get script revisions');
      }
    },
    async ADD_SCRIPT_REVISION(context, scriptRevision) {
      const response = await fetch(`${makeURL('/api/v1/show/script/revisions')}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(scriptRevision),
      });
      if (response.ok) {
        context.dispatch('GET_SCRIPT_REVISIONS');
        Vue.$toast.success('Added new script revision!');
      } else {
        console.error('Unable to add new script revision');
        Vue.$toast.error('Unable to add new script revision');
      }
    },
    async DELETE_SCRIPT_REVISION(context, revisionID) {
      const response = await fetch(`${makeURL('/api/v1/show/script/revisions')}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          rev_id: revisionID,
        }),
      });
      if (response.ok) {
        context.dispatch('GET_SCRIPT_REVISIONS');
        Vue.$toast.success('Deleted script revision!');
      } else {
        console.error('Unable to delete script revision');
        Vue.$toast.error('Unable to delete script revision');
      }
    },
    async LOAD_SCRIPT_REVISION(context, revisionID) {
      const response = await fetch(`${makeURL('/api/v1/show/script/revisions/current')}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          new_rev_id: revisionID,
        }),
      });
      if (response.ok) {
        context.dispatch('GET_SCRIPT_REVISIONS');
        Vue.$toast.success('Loaded script revision!');
      } else {
        console.error('Unable to load script revision');
        Vue.$toast.error('Unable to load script revision');
      }
    },
    async SCRIPT_REVISION_CHANGED(context) {
      await context.dispatch('GET_SCRIPT_REVISIONS');
      /* eslint-disable no-await-in-loop, no-restricted-syntax */
      for (const page of Object.keys(context.state.script)) {
        await context.dispatch('LOAD_SCRIPT_PAGE', page);
        await context.dispatch('ADD_BLANK_PAGE', page);
      }
      /* eslint-enable no-await-in-loop, no-restricted-syntax */
    },
    async LOAD_SCRIPT_PAGE(context, page) {
      const searchParams = new URLSearchParams({
        page,
      });
      const response = await fetch(`${makeURL('/api/v1/show/script')}?${searchParams}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (response.ok) {
        const respJson = await response.json();
        context.commit('SET_SCRIPT_PAGE', {
          pageNumber: respJson.page,
          page: respJson.lines,
        });
      } else {
        console.error('Unable to load script page');
      }
    },
  },
  getters: {
    SCRIPT_REVISIONS(state) {
      return state.revisions;
    },
    CURRENT_REVISION(state) {
      return state.currentRevision;
    },
    GET_SCRIPT_PAGE: (state) => (page) => {
      const pageStr = page.toString();
      if (Object.keys(state.script).includes(pageStr)) {
        return state.script[pageStr];
      }
      return [];
    },
  },
};
