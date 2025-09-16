import { useState } from 'react';
import './App.css'
import ImageCarousel from './components/image-carousel'
import DataTable from './components/DataTable';
import FileExplorer from './components/FileExplorer';
import TicTacToe from './components/TicTocToe';
import BarContainer from './components/ProgressBar';
import ModalDialog from './components/ModalDialog';
// const images = [
//   {
//     src: 'https://picsum.photos/id/600/600/400',
//     alt: 'Forest',
//   },
//   {
//     src: 'https://picsum.photos/id/100/600/400',
//     alt: 'Beach',
//   },
//   {
//     src: 'https://picsum.photos/id/200/600/400',
//     alt: 'Yak',
//   },
//   {
//     src: 'https://picsum.photos/id/300/600/400',
//     alt: 'Hay',
//   },
//   {
//     src: 'https://picsum.photos/id/400/600/400',
//     alt: 'Plants',
//   },
//   {
//     src: 'https://picsum.photos/id/500/600/400',
//     alt: 'Building',
//   },
// ];

// const data = [
//     {
//       id: 1,
//       name: 'README.md',
//     },
//     {
//       id: 2,
//       name: 'Documents',
//       children: [
//         {
//           id: 3,
//           name: 'Word.doc',
//         },
//         {
//           id: 4,
//           name: 'Powerpoint.ppt',
//         },
//       ],
//     },
//     {
//       id: 5,
//       name: 'Downloads',
//       children: [
//         {
//           id: 6,
//           name: 'unnamed.txt',
//         },
//         {
//           id: 7,
//           name: 'Misc',
//           children: [
//             {
//               id: 8,
//               name: 'foo.txt',
//             },
//             {
//               id: 9,
//               name: 'bar.txt',
//             },
//           ],
//         },
//       ],
//   },
// ]

function App() {
  const [open, setOpen] = useState(false)

  return (
    <div>
      <button onClick={() => setOpen(!open)}>Open dialog</button>
      <ModalDialog title={'title'} open={open} setOpen={setOpen}>
        One morning, when Gregor Samsa woke from troubled
        dreams, he found himself transformed in his bed into
        a horrible vermin. He lay on his armour-like back,
        and if he lifted his head a little he could see his
        brown belly, slightly domed and divided by arches
        into stiff sections.
      </ModalDialog>
    </div>
  )
}

export default App
