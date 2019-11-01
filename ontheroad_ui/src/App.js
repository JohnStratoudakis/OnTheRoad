import React from 'react';

import axios from 'axios';

import './App.css';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {results: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        console.log('handleChange(event)');
        this.setState({results: event.target.value});
    }

    handleSubmit(event) {
        console.log("Handle Submit Event");
        console.log(`this.state: ${this.state}`);
        console.log(`event: ${typeof(event)}`);

        // TODO: Read this from config or env var
        var serverHost = "127.0.0.1";
        console.log(`Server Host Name: ${serverHost}`);

        // TODO: Read this from form
        var request = {
            "locations": [
                ["Amsterdam", "Amsterdam, The Netherlands"],
                ["London", "London, England"],
                ["Brussels", "Brussels, Belgium"]
            ]
        };
        axios.post(`http://127.0.0.1:5000/onTheRoad`, request )
              .then(res => {
                      console.log(res);
                              console.log(res.data);
                                    });

        var results = "Results of TSP";
        this.setState({results: results});
        event.preventDefault();
    }

    render() {
        var placeholder = "Amsterdam, The Netherlands\nBrussels, Belgium\nLondon, England";
        return (
            <div className="App">
                <header className="App-header">
                    <form onSubmit={this.handleSubmit}>
                        <label>Euro Trip Calculator</label>
                        <br />
                        <textarea placeholder={placeholder}
                                  onBlur={this.handleChange.bind(this)}
                                  rows='8'
                                  cols='30'
                            ></textarea>
                        <input type="submit" value="Submit" />
                    </form>
                    Recommended Trip Order:
                    <br />
                    {this.state.results}
                </header>
            </div>
        );
    }
}

export default App;
