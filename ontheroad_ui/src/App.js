import React from 'react';

import Button from 'react-bootstrap/Button';
import Table from 'react-bootstrap/Table';

import axios from 'axios';

import Location from './Location.js';

import './App.css';

require('dotenv').config();


class App extends React.Component {
    serverString = "";

    constructor(props) {
        super(props);
        if(process.env.NODE_ENV == "production") {
            this.serverString = "https://www.johnstratoudakis.com/OnTheRoad";
        } else {
            this.serverString = "http://127.0.0.1:5000"
        }
        console.log("serverString: " + this.serverString);
        console.log("NODE_ENV: " + process.env.NODE_ENV);

        // Dump all environment variables
        /*
        console.log('Dump all environment variables');
        Object.keys(process.env).forEach(function(key) {
              console.log('App.js: ' + key + '="' + process.env[key] +'"');
        });
        */

        let addresses_storage = window.localStorage.getItem("addresses");
        if(addresses_storage === null) {
            console.log(`No addresses found in localStorage...`);
            addresses_storage = [];
        } else {
            console.log(`Loading addresses from localStorage...`);
            addresses_storage = JSON.parse(addresses_storage);
//            for(var i=0; i<addresses_storage.length; i++) {
//                console.log(`address_storage[${i}]: ${addresses_storage[i][2]}`);
//            }
        }

        this.handleCalculate = this.handleCalculate.bind(this);
        this.handleClear = this.handleClear.bind(this);
        this.handleOnAddressesChange = this.handleOnAddressesChange.bind(this);
        this.handleOnStartingIndexChange = this.handleOnStartingIndexChange.bind(this);

        this.state = {
          results: ['', ''],
          addresses: addresses_storage,
          startingIndex: 0
        };
    }

    componentDidMount() {
        console.log("componentDidMount()");
        let addresses_storage = window.localStorage.getItem("addresses");
        console.log(`RAW_ADDRESSES: ${addresses_storage}`);
        addresses_storage = JSON.parse(addresses_storage);
        this.setState({addresses: addresses_storage});
    }

//    componentDidUpdate(prevProps, prevState) {
//        console.log("componentDidUpdate");
//    }

    dump_test(addresses) {
      console.log(`addresses.length: ${addresses.length}`);
      for(var i=0; i < addresses.length; i++) {
        var element = addresses[i];
        console.log(`element.length: ${element.length}`)
        for(var j=0; j < element.length; j++) {
          console.log(`addresses[${i}][${j}]: ${addresses[i][j]}`);
        }
      }
    }

    handleCalculate(event) {
        console.log("App.js::handleCalculate()");

        var request_addresses = [];
        var addresses = this.state.addresses;
        var startingIndex = this.state.startingIndex;
        console.log(`addresses.length: ${addresses.length}`);
        console.log(`startingIndex: ${startingIndex}`);
        for(var i=0; i < addresses.length; i++) {
            console.log(`addresses[${i}][2]: ${addresses[i][2]}`);
            request_addresses.push( [ addresses[i][2], addresses[i][2], (startingIndex == i)] );
        }

        var request = {
            "locations": request_addresses
        };
        console.log("Server String: " + this.serverString);
        console.log("Sending request: " + request.locations);

        // Make request
        axios.post(`${this.serverString}`, request )
            .then(res => {
                var results_array = [];
                for(var i=0; i < res.data['best_path'].length; i++) {
                    results_array.push(res.data['best_path'][i]);
                    console.log(`Path[${i}][0]: ${res.data['best_path'][i][0]}`)
                    console.log(`Path[${i}][1]: ${res.data['best_path'][i][1]}`)
                }

                this.setState({results: results_array});
            });
        event.preventDefault();
    }

    handleClear(event) {
        console.log("handleClear() event");

        console.log("Clearing local storage.");
        window.localStorage.setItem("addresses", JSON.stringify([]));

        console.log("Clearing addresses.");
        this.setState({addresses: []});
    }

    handleOnAddressesChange(new_addresses) {
        console.log(`handleOnAddressChange(${new_addresses})`);
        this.setState({addresses: new_addresses});
    }

    handleOnStartingIndexChange(new_startingIndex) {
        console.log(`handleOnStartingIndexChange(${new_startingIndex})`);
        this.setState({startingIndex: new_startingIndex});
    }

    render() {
        const addresses = this.state.addresses;
        const startingIndex = this.state.startingIndex;

        console.log("App::render()");
        return (
            <div className="App" style={{width: '100%'}}>
                <header className="App-header">
                    <div style={{ position: 'relative', width: '100%'}}>
                    <br />
                    <Location
                        addresses={addresses}
                        onAddressesChange={this.handleOnAddressesChange}
                        startingIndex={startingIndex}
                        onStartingIndexChange={this.handleOnStartingIndexChange}
                     />
                    </div>
                    <div>
                        <Table bordered hover variant="dark">
                            <tbody>
                                <tr>
                                    <td>
                                        <Button variant="secondary" onClick={this.handleCalculate} size="me">Calculate Best Path</Button>
                                    </td>
                                    <td>
                                        <Button variant="secondary" onClick={this.handleClear} size="me">Clear</Button>
                                    </td>
                                </tr>
                            </tbody>
                        </Table>
                    </div>

                    <br />
                    <h3>Recommended Trip Order:</h3>
                    {
                    <div>
                    {
                        this.state.results.map((city, idx) => 
                            <div key={idx} className={ App.row }>
                                <div>
                                    <h4>{ city[0] }</h4><h6>{city[1]}</h6>
                                </div>
                            </div>
                        )
                    }
                    </div>
                    }
                </header>
            </div>
        );
    }
}

export default App;
