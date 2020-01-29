import React from 'react';

import Button from 'react-bootstrap/Button';
import Table from 'react-bootstrap/Table';

import { hello_world, sum } from './helpers';
//import axios from 'axios';

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

//    handleChange(event) {
//        var addr_array = [];
//
//        var addresses = event.target.value.split('\n');
//        addresses.forEach(function(val,index,array){
//            var name = array[index].split(',')[0];
//            var address = array[index];
//            var new_location = [name, address];
//            addr_array.push( new_location );
//            console.log(`Adding address[${index}]: ` + new_location);
//        });
//        this.setState({results: addr_array});
//    }
//
//    handleSubmit(event) {
//        console.log("handleSubmit()...");
//        console.log(`this.state: ${this.state}`);
//        console.log(`event: ${typeof(event)}`);
//
//        // TODO: Read this from form
//        var results = this.state['results'];
//        var request = {
//            "locations": results
//        };

//        console.log("RESULTS: " + results);
//        console.log("RESULTS: " + results.length);
//        //var addresses = results.split('\n');
//        /*
//        addresses.forEach(function(val,index,array){
//            var name = array[index].split(',')[0];
//            var address = array[index];
//            var new_location = new Array(name, address);
//            //addr_array.push( new_location );
//            console.log(`Address[${index}]: ` + new_location);
//        });
//*/
//        console.log("this.state['results']: " + this.state['results']);
////        request['locations'].push( ["Amsterdam", "--------Amsterdam, The Netherlands"] );
//        console.log("Sending the following request: " + request);
//        console.log(`Sending the following request ${request}`);
//        console.log(request);
//
//        //axios.post(`https://${this.serverHost}:${this.serverPort}/onTheRoad`, request )
//        axios.post(`https://${this.serverHost}/onTheRoad`, request )
//            .then(res => {
//                console.log("DUMPING res");
//                console.log(res);
//                console.log("DUMPING res.data");
//                console.log(res.data);
//                console.log("DUMPING res.data.best_path");
//                console.log(res.data['best_path']);
//                var results_text = "Results of TSP";
//                results_text = res.data['best_path'];
//                //console.log("RESULTS OF TSP: " + res);
//                this.setState({results: results_text});
//            });
//
//        event.preventDefault();
//    }
//
//    getPlace(address, placeID) {
//        this.saveAddress(address, placeID)
//        geocodeByAddress(address)
//          .then(results => getLatLng(results[0]) )
//          .then(latlng => this.saveLocation(latlng) )
//          .catch(error => console.error('Error', error))
//    }
    constructor(props) {
        super(props);
        this.onCalculate = this.onCalculate.bind(this);
        this.handleOAddressesChange = this.handleOnAddressesChange.bind(this);
        //this.dump_test = this.dump_test.bind(this);
        this.state = {
          results: 'res',
          addresses: [],
          guests: [
              {name:'Paris', address:'Paris, France'},
              {name:'Amsterdam', address:'Amsterdam, The Netherlands'},
              {name:'Brussels', address:'Brussels, Belgium'},
          ]
        };
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

    onCalculate(event) {
        console.log("onCalculate()");
        //console.log(`${event.toString()}`);

        this.dump_test(this.Location.state.allAddresses);
    }

    handleOnAddressesChange(new_addresses) {
        console.log("App.handleOnAddressesChange()");
        console.log(`new_addresses.length: ${new_addresses.length}`);
        for(var i=0; i < new_addresses.length; i++) {
            var element = new_addresses[i];
            console.log(`element.length: ${element.length}`)
            for(var j=0; j < element.length; j++) {
                console.log(`new_addresses[${i}][${j}]: ${new_addresses[i][j]}`);
            }
        }
        hello_world();
        //this.dump_test(new_addresses);
        //this.setState({addresses: addresses});
    }

    render() {
        const addresses = this.state.addresseses;
        return (
            <div className="App" style={{width: '100%'}}>
                <header className="App-header">
                    {/*
                    Recommended Trip Order:
                    <br />
                    Paris, France -> Amsterdam, The Netherlands
                    <br />
                    {
                        this.state.results
                    }
                    */}
                    {/*
                    <div>
                    {this.state.guests.map((guest, idx) => 
                        <div className={ App.row }>
                            <div>
                                <h4>{ guest.address }</h4>
                            </div>
                        </div>
                    )}
                    </div>
                    */}
                    <br />
                    <div style={{ position: 'relative', width: '100%'}}>
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
                                        <Button variant="secondary" onClick={this.onCalculate} size="me">Calculate Best Path</Button>
                                    </td>
                                </tr>
                            </tbody>
                        </Table>
                    </div>
                </header>
            </div>
        );
    }
}

export default App;