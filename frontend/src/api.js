class Api {

  async getToken (username, password) {
    const res = await fetch(
      'http://127.0.0.1:8000/api-token-auth/',
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
      'http://127.0.0.1:8000/api/games/games',
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
