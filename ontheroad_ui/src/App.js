import React from 'react';


import axios from 'axios';

import './App.css';

require('dotenv').config();

class App extends React.Component {

    serverHost = process.env.REACT_APP_HOST_IP;
    serverPort = "5000";

    constructor(props) {
        super(props);
        this.state = {results: ''};

        
        this.serverHost = process.env.REACT_APP_HOST_IP;
        this.serverPort = "5000";
        
        if(this.serverHost)
        {
            console.log(`REACT_APP_HOST_IP=${process.env.REACT_APP_HOST_IP}`);
        }
        else
        {
            this.serverHost="www.johnstratoudakis.com";
            this.serverPort="443";
        }

        console.log(`Setting this.serverHost: ${this.serverHost}.`);
        console.log(process.env);

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        var addr_array = [];

        var addresses = event.target.value.split('\n');
        addresses.forEach(function(val,index,array){
            var name = array[index].split(',')[0];
            var address = array[index];
            var new_location = [name, address];
            addr_array.push( new_location );
            console.log(`Adding address[${index}]: ` + new_location);
        });
        this.setState({results: addr_array});
    }

    handleSubmit(event) {
        console.log("handleSubmit()...");
        console.log(`this.state: ${this.state}`);
        console.log(`event: ${typeof(event)}`);

        //console.log("this.state: " + this.state);
        //console.log("this.state: " + typeof(this.state));
        //console.log(`typeof(this.state): ${typeof(this.state.toString())}`);
        // TODO: Read this from config or env var
//        var serverHost = "127.0.0.1";
        //console.log(`Server Host Name: ${serverHost}`);

        // TODO: Read this from form
        var results = this.state['results'];
        var request = {
            "locations": results
//                ["Amsterdam", "Amsterdam, The Netherlands"],
//                ["London", "London, England"],
//                ["Brussels", "Brussels, Belgium"]
//            ]
        };

        console.log("RESULTS: " + results);
        console.log("RESULTS: " + results.length);
        //var addresses = results.split('\n');
        /*
        addresses.forEach(function(val,index,array){
            var name = array[index].split(',')[0];
            var address = array[index];
            var new_location = new Array(name, address);
            //addr_array.push( new_location );
            console.log(`Address[${index}]: ` + new_location);
        });
*/
        console.log("this.state['results']: " + this.state['results']);
//        request['locations'].push( ["Amsterdam", "--------Amsterdam, The Netherlands"] );
        console.log("Sending the following request: " + request);
        console.log(`Sending the following request ${request}`);
        console.log(request);

        axios.post(`https://${this.serverHost}:${this.serverPort}/onTheRoad`, request )
            .then(res => {
                console.log("DUMPING res");
                console.log(res);
                console.log("DUMPING res.data");
                console.log(res.data);
                console.log("DUMPING res.data.best_path");
                console.log(res.data['best_path']);
                var results_text = "Results of TSP";
                results_text = res.data['best_path'];
                //console.log("RESULTS OF TSP: " + res);
                this.setState({results: results_text});
            });


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
