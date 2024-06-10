import React from 'react'
import { VarCard } from './Cards/variantCard'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      variants: 'loading',
      loaded: false
    }
  }

  componentDidMount() {
    fetch('http://localhost:8080/variants/', {
      method: "GET", 
      headers : {
        'mode' : 'no-cors',
        'Content-Type': 'application/json',
        },
      }
    )
    .then(responce => responce.json())
    .then(data => this.setState({variants: data}))

    console.log(this.state.variants, typeof(this.state.variants))
  }

  loadVariants = () => {
    this.setState({loaded : true})
    console.log(this.state.variants)
  }

   render() {
    const {variants, loaded} = this.state
    if (!loaded) {
      return (
      <>
      <p>Loading</p>
      <button onClick={this.loadVariants}>load variants</button>
      </>
      )
    } else {
      return (
        <>
        <h1>Fetched data</h1>
        <div> {variants.map(variant => <VarCard
        key = {variant.id}
        exonic = {variant.exonic}
        chromosome = {variant.chromosome}
        position = {variant.position}
        gene = {variant.gene}
        consequence = {variant.consequence}
        depth = {variant.depth}/>
        )}</div>
        </>
      );
    };
   }
}

export default App