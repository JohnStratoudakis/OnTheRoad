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
//        console.log('handleChange(event)');
//        console.log("this.state: " + this.state);
//        console.log("this.state['results']: " + this.state['results']);
//        console.log("this.state: " + typeof(this.state));
//        console.log(`typeof(this.state): ${typeof(this.state.toString())}`);
//        console.log("=======");
        var addr_array = [];

        var addresses = event.target.value.split('\n');
        addresses.forEach(function(val,index,array){
            var name = array[index].split(',')[0];
            var address = array[index];
            var new_location = [name, address];
            addr_array.push( new_location );
            console.log(`Address[${index}]: ` + new_location);
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
        var serverHost = "127.0.0.1";
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

        axios.post(`http://${serverHost}:5000/onTheRoad`, request )
              .then(res => {
                      console.log(res);
                              console.log(res.data);
                                    });

        var results_text = "Results of TSP";
        console.log("RESULTS OF TSP: " + res);
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
