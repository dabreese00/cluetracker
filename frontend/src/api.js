class Api {

  async getToken (username, password) {
    const res = await fetch(
      process.env.REACT_APP_API_TOKEN_ENDPOINT,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({username: username, password: password})
      }
    );
    const res_data = await res.json();
    return res_data.token
  }

  async listGames (token) {
    const res = await fetch(
      process.env.REACT_APP_API_GAMES_LIST_ENDPOINT,
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
