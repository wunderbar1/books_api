import React, { Component } from 'react'

class Login extends Component {

  state = {
    cridentials: {username: '', password: ''}
  }

  login = event =>{
    console.log(this.state.cridentials);
    fetch('http://127.0.0.1:8000/auth/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(this.state.cridentials)
    })
    .then(data => data.json())
    .then(
      data => {
        console.log(data.token);
      }
    ).catch( error => console.log(error))
  }

  inputChanged = event =>{
    const cred = this.state.cridentials;
    cred[event.target.name] = event.target.value;
    this.setState({credentials: cred})
  }

  render(){
    return (
        <div>
            <h1> Login User </h1>
            <label>
              username:
              <input type="text" name="username" value={this.state.cridentials.username}
              onChange={this.inputChanged}/>
              password:
              <input type="password" name="password" value={this.state.cridentials.password}
              onChange={this.inputChanged}/>
            </label>
            <button onClick={this.login}>Login</button>

        </div>
  );
}
}
export default Login;