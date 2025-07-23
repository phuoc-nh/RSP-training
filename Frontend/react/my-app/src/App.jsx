import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Accordion from './components/accordion'
import Booker from './components/flight-booker'
import Sol from './components/sol'

function App() {

  return (
    <Booker></Booker>
    // <Sol></Sol>
    // <div className="wrapper">
    //   <Accordion
    //     sections={[
    //       {
    //         value: 'html',
    //         title: 'HTML',
    //         contents:
    //           'The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser.',
    //       },
    //       {
    //         value: 'css',
    //         title: 'CSS',
    //         contents:
    //           'Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML.',
    //       },
    //       {
    //         value: 'javascript',
    //         title: 'JavaScript',
    //         contents:
    //           'JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.',
    //       },
    //     ]}
    //   />
    // </div>
  )
}

export default App
