import React from 'react';
//import axios from 'axios';

//import PlacesAutocomplete from 'react-places-autocomplete';
//import {
//    geocodeByAddress,
//    geocodeByPlaceId,
//    getLatLng
//} from 'react-places-autocomplete';

//import {add_guest} from '../../store/reducers';
//import MapWithRestaurant from '../destination/map.js';

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
        this.state = {
          address: '',
          results: '',
          value: ''
        };
//        this.state = {results: '', address: '731 Lexington Avenuew, New York, NY', value: 'Default_Value'};
//        this.onChange = (address) => this.setState({ address, placeID: null, latlng: null, guest: null })
//        this.serverHost = process.env.REACT_APP_HOST_IP;
//        this.serverPort = "5000";

//        this.getPlace = this.getPlace.bind(this)

//        if(this.serverHost) {
//            console.log(`REACT_APP_HOST_IP=${process.env.REACT_APP_HOST_IP}`);
//        } else {
//            this.serverHost="www.johnstratoudakis.com";
//            this.serverPort="443";
//        }

//        console.log(`Setting this.serverHost: ${this.serverHost}.`);
//        console.log(process.env);

        //this.handleChange = this.handleChange.bind(this);
//        this.handleSubmit = this.handleSubmit.bind(this);
//        this.handleChange = this.handleChange2.bind(this);
//        this.handleSelect = this.handleSelect2.bind(this);
    }

//    handleChange2 = address => {
//        console.log(`handleChange2(event)`);
//        this.setState({ address });
//    };
//
//    handleSelect2 = address => {
//        console.log(`handleSelect2(event)`);
//        geocodeByAddress(address)
//            .then(results => getLatLng(results[0]))
//            .then(latLng => console.log('Success', latLng))
//            .catch(error => console.error('Error', error));
//    };

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
//
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

    render() {
//        var placeholder = "Amsterdam, The Netherlands\nLondon, England\nBrussels, Belgium\nFrankfurt, Germany\nParis, France";

//        const {lat, lng} = this.state.latlng || {}
//        const inputProps = {
//            value: this.state.address,
//            onChange: this.onChange
//        }

        return (
            <div className="App">
                <header className="App-header">
{/*
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
*/}
                    Recommended Trip Order:
                    <br />
                    {/*this.state.results*/}
                    <br />
                    My custom areas:
                    <div style={{ position: 'relative'}}>
{/*
                        <PlacesAutocomplete
                            value={this.state.address}
                            onChange={this.onChange}
                            onSelect={this.handleSelect2}
                            styles={ defaultStyles }>
                        {({ getInputProps, suggestions, getSuggestionItemProps, loading }) => (
          <div>
            <input
              {...getInputProps({
                placeholder: 'Search Places ...',
                className: 'location-search-input',
              })}
            />
            <div className="autocomplete-dropdown-container">
              {loading && <div>Loading...</div>}
              {suggestions.map(suggestion => {
                const className = suggestion.active
                  ? 'suggestion-item--active'
                  : 'suggestion-item';
                // inline style for demonstration purpose
                const style = suggestion.active
                  ? { backgroundColor: '#fafafa', cursor: 'pointer' }
                  : { backgroundColor: '#ffffff', cursor: 'pointer' };
                return (
                  <div
                    {...getSuggestionItemProps(suggestion, {
                      className,
                      style,
                    })}
                  >
                    <span>{suggestion.description}</span>
                  </div>
                );
              })}
            </div>
          </div>
                        )}
                        </PlacesAutocomplete>
*/}
                    </div>
                </header>
            </div>
        );
    }
}

export default App;