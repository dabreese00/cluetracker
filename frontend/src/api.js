class Api {

  constructor() {
    this.token_endpoint = process.env.REACT_APP_API_TOKEN_ENDPOINT;
    this.games_list_endpoint = process.env.REACT_APP_API_GAMES_LIST_ENDPOINT;
    this.content_type = 'application/json;charset=utf-8';
  }

  async getToken (username, password) {
    const res = await fetch(
      this.token_endpoint,
      {
        method: 'POST',
        headers: {
          'Content-Type': this.content_type
        },
        body: JSON.stringify({username: username, password: password})
      }
    );
    const res_data = await res.json();
    return res_data.token
  }

  async listGames (token) {
    const res = await fetch(
      this.games_list_endpoint,
      {
        headers: {
          Authorization: 'Token ' + token
        }
      }
    );
    return await res.json();
  }
}

export default Api;
