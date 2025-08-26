import { useState } from 'react';
import './App.css'
import ImageCarousel from './components/image-carousel'

const images = [
  {
    src: 'https://picsum.photos/id/600/600/400',
    alt: 'Forest',
  },
  {
    src: 'https://picsum.photos/id/100/600/400',
    alt: 'Beach',
  },
  {
    src: 'https://picsum.photos/id/200/600/400',
    alt: 'Yak',
  },
  {
    src: 'https://picsum.photos/id/300/600/400',
    alt: 'Hay',
  },
  {
    src: 'https://picsum.photos/id/400/600/400',
    alt: 'Plants',
  },
  {
    src: 'https://picsum.photos/id/500/600/400',
    alt: 'Building',
  },
];
function App() {
const [message, setMessage] = useState('Image Carousel');
  return (
   <div className='container'>
      <h1>{message}</h1>
      <ImageCarousel images={images} />
    </div>
  )
}

export default App
