import React from 'react';
import './App.css';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {value: 'coconut'};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        console.log('handleChange(event)');
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        console.log("Handle Submit Event");
        console.log("this.state: {this.state}");
        console.log("event: {typeof(event)}");
        event.preventDefault();
        //this.out.value = "DDDD";
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
                    {this.state.value}
                </header>
            </div>
        );
    }
}

export default App;
