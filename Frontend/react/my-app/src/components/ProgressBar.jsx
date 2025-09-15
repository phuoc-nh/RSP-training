import { useEffect, useState } from "react";

// function ProgressBar() {
//   const [startTransition, setStartTransition] =
//     useState(false);

//   // Start transition after first render and never
//   // apply this effect ever again.
//   useEffect(() => {
//     if (startTransition) {
//       return;
//     }

//     setStartTransition(true);
//   });

//   return (
//     <div className="bar">
// 		  <div
// 			  className={`bar-contents ${startTransition && 'bar-contents--filled' }`}
//       />
//     </div>
//   );
// }

// export default function BarContainer() {
//   const [bars, setBars] = useState(0);

//   return (
//     <div className="wrapper">
//       <div>
//         <button
//           onClick={() => {
//             setBars(bars + 1);
//           }}>
//           Add
//         </button>
//       </div>
//       <div className="bars">
//         {Array(bars)
//           .fill(null)
//           .map((_, index) => (
//             <ProgressBar key={index} />
//           ))}
//       </div>
//     </div>
//   );
// }

const Bar = () => {
	const [startTransition, setStartTransition] = useState(false)
	useEffect(() => {
		if (startTransition) return

		setStartTransition(true)
	}, [])

  return <div className={`bar ${startTransition && 'bar--filled'}`}></div>;
};

export default function BarContainer() {
  const [bars, setBars] = useState(0);
	console.log('bars', bars)
  return (
    <div>
      <button onClick={() => setBars(bars + 1)}>Add</button>
		  <div className="bar-container">
			  {/* <Bar></Bar>
			  <Bar></Bar>
			  <Bar></Bar> */}
        {Array(bars).fill(null).map((el, key) => {
          return <Bar key={key}></Bar>;
        })}
      </div>
    </div>
  );
}
