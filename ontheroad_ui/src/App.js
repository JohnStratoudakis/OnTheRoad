import React from 'react';

import Button from 'react-bootstrap/Button';
import Table from 'react-bootstrap/Table';

import axios from 'axios';

import Location from './Location.js';

import './App.css';

require('dotenv').config();

//const defaultStyles = {
//    root: {
//      position: 'relative',
//      paddingBottom: '0px',
//    },
//    input: {
//      display: 'inline-block',
//      width: '100%',
//      padding: '10px',
//    },
//    autocompleteContainer: {
//      position: 'absolute',
//      top: '100%',
//      backgroundColor: 'white',
//      border: '1px solid #555555',
//      width: '100%',
//    },
//    autocompleteItem: {
//      backgroundColor: '#ffffff',
//      padding: '10px',
//      color: '#555555',
//      cursor: 'pointer',
//    },
//    autocompleteItemActive: {
//      backgroundColor: '#fafafa'
//    },
//    googleLogoContainer: {
//      textAlign: 'right',
//      padding: '1px',
//      backgroundColor: '#fafafa'
//    },
//    googleLogoImage: {
//      width: 150
//    }
//  }

class App extends React.Component {
    serverHost = process.env.REACT_APP_HOST_IP;
    serverPort = "5000";

    constructor(props) {
        super(props);
        console.log("App.js:constructor()");
        if(this.serverHost === undefined) {
            this.serverHost = "localhost";
        }
        Object.keys(process.env).forEach(function(key) {
              console.log('export ' + key + '="' + env[key] +'"');
        });
        console.log(`App.js:serverHost: ${this.serverHost}`);
        console.log(`App.js:process.env: ${process.env}`);
        console.log(`App.js:process.env.toString(): ${process.env.toString()}`);
        for(var en in process.env) {
            console.log(`App.js:.e: ${en}`);
        }

        let addresses_storage = window.localStorage.getItem("addresses");
        if(addresses_storage === null) {
            console.log(`No addresses found in localStorage...`);
            addresses_storage = [];
        } else {
            console.log(`Loading addresses from localStorage...`);
            addresses_storage = JSON.parse(addresses_storage);
            for(var i=0; i<addresses_storage.length; i++) {
                console.log(`address_storage[${i}]: ${addresses_storage[i][2]}`);
            }
        }

        this.handleCalculate = this.handleCalculate.bind(this);
        this.handleClear = this.handleClear.bind(this);
        this.handleOnAddressesChange = this.handleOnAddressesChange.bind(this);

        this.state = {
          results: ['', ''],
          addresses: addresses_storage
        };
    }

    componentDidMount() {
        console.log("componentDidMount()");
        let addresses_storage = window.localStorage.getItem("addresses");
        console.log(`RAW_ADDRESSES: ${addresses_storage}`);
        addresses_storage = JSON.parse(addresses_storage);
        this.setState({addresses: addresses_storage});
    }

    componentDidUpdate(prevProps, prevState) {
        console.log("componentDidUpdate");
    }

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
        console.log("handleCalculate()");

        var request_addresses = [];
        var addresses = this.state.addresses;
        console.log(`addresses.length: ${addresses.length}`);
        for(var i=0; i < addresses.length; i++) {
            console.log(`addresses[${i}][2]: ${addresses[i][2]}`);
            request_addresses.push( [ addresses[i][2], addresses[i][2] ] );
        }
/*
        // Now create request
        request_addresses = [];

        request_addresses.push(["Astoria Bier", "31-14 Broadway, Astoria, NY"])
        request_addresses.push(["Minos", "22-27 33rd Street, Astoria, NY"])
        request_addresses.push(["Omonoia", "32-33 31st Street, Astoria, NY"])
        request_addresses.push(["BxSci", "75 West 205th Street, Bronx, NY"])
        request_addresses.push(["Lex", "731 Lexington Ave, New York, NY"])
        request_addresses.push(["Apt", "31-36 28th Road, Astoria, NY"])
        request_addresses.push(["Flushing", "40-20 195th Street, Flushing, NY"])
// */
/*
        request_addresses.push(["Vienna", "Vienna, Austria"])
        request_addresses.push(["Budapest", "Budapest, Hungary"])
        request_addresses.push(["Bratislava", "Bratislava, Slovakia"])
        request_addresses.push(["Zagreb", "Zagreb, Serbia"])
        request_addresses.push(["Prague", "Prague, Czech Republic"])
//        */

        /*
        request_addresses.push(["Paris", "Paris, France"])
        request_addresses.push(["Amsterdam", "Amsterdam, The Netherlands"])
        request_addresses.push(["Brussels", "Brussels, Belgium"])
        request_addresses.push(["Prague", "Prague, Czech Republic"])
        request_addresses.push(["Vienna", "Vienna, Austria"])
        request_addresses.push(["Bratislava", "Bratislava, Slovakia"])
        request_addresses.push(["Budapest", "Budapest, Hungary"])
*/

        var request = {
            "locations": request_addresses
        };
        console.log("Server Host: " + this.serverHost);
        console.log("Sending request: " + request.locations);

        // Make request
        axios.post(`https://${this.serverHost}/onTheRoad`, request )
            .then(res => {
//                console.log("DUMPING res");
//                console.log(res);
//                console.log("DUMPING res.data");
//                console.log(res.data);
//                console.log("DUMPING res.data.best_path");
//                console.log(res.data['best_path']);

                var results_array = [];
                for(var i=0; i < res.data['best_path'].length; i++) {
                    results_array.push(res.data['best_path'][i]);
                    console.log(`Path[${i}][0]: ${res.data['best_path'][i][0]}`)
                    console.log(`Path[${i}][1]: ${res.data['best_path'][i][1]}`)
                }

                //var results_text = "Results of TSP";
                //results_text = res.data['best_path'];
                //console.log("RESULTS OF TSP: " + res);
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
        console.log("App.handleOnAddressesChange()");
        //console.log(`new_addresses.length: ${new_addresses.length}`);
//        for(var i=0; i < new_addresses.length; i++) {
//            var element = new_addresses[i];
//            console.log(`element.length: ${element.length}`)
//            for(var j=0; j < element.length; j++) {
//                console.log(`new_addresses[${i}][${j}]: ${new_addresses[i][j]}`);
//            }
//        }
        this.setState({addresses: new_addresses});
    }

    render() {
        const addresses = this.state.addresses;
        console.log("App::render()");
        console.log(`App::render():addresses`);
        //for(var i=0; i<addresses.length; i++) {
        //    console.log(`addresses[${i}]: ${addresses[i][2]}`);
        //}
        return (
            <div className="App" style={{width: '100%'}}>
                <header className="App-header">
                    <br />
                    <div style={{ position: 'relative', width: '100%'}}>
                    <h5>Location</h5>
                    <h3>Local Storage DEBUG_11 INFO:</h3>
                    <div>
                    {
                        addresses && addresses.map((city, idx) => 
                            <div key={idx} className={ App.row }>
                                <div>
                                    <h4>{ city[2] }</h4>
                                </div>
                            </div>
                        )
                    }
                    </div>
                    <Location
                        addresses={addresses}
                        onAddressesChange={this.handleOnAddressesChange}
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
