import React, {Component} from 'react';
import Script from 'react-load-script';
import axios from 'axios';

class Login extends Component{
    onSuccess = (googleUser) => {
        console.log('Logged in as: ' + googleUser.getBasicProfile().getName());

        let id_token = googleUser.getAuthResponse().id_token;
        // console.log('data', googleUser.getAuthResponse())

        let url = `http://127.0.0.1:8000/accounts/auth/login`
        axios.post(url, {'token': id_token} )
            .then((response) => {
                console.log(response.data)
            })
            .catch((error) => {
                console.log(error)
            })

      }
    onFailure = (error) => {
        console.log(error);
      }
    renderButton = () => {
        gapi.signin2.render('my-signin2', {
          'scope': 'profile email',
          'width': 240,
          'height': 50,
          'longtitle': true,
          'theme': 'dark',
          'onsuccess': this.onSuccess,
          'onfailure': this.onFailure
        });
      }

    signOut = () =>  {
        let auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then( () => {
          console.log('User signed out.');
        });
      }

    render () {
        return (
            <div>
            <div id="my-signin2" />
            <Script url="https://apis.google.com/js/platform.js"
                    onLoad={this.renderButton} 
                    attributes = {{"async" : "",  "defer" : ""}}
            
            />
            <button onClick={this.signOut}>Log Out </button>
            </div>
        
    )
}
}

export default Login