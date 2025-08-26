import React, { useState } from "react";

export default function ImageCarousel({ images }) {
	let [index, setIndex] = useState(0)

	const handlePrev = () => {
		let newIndex = index -= 1
		if (newIndex < 0) {
			newIndex = images.length - 1
		}
		setIndex(newIndex)
	}

	const handleNext = () => {
		let newIndex = index += 1
		if (newIndex >= images.length) {
			newIndex = 0
		}
		setIndex(newIndex)
	}

	return (
		<div className="carousel">
			<div className="carousel-image">

			{images.map(({ alt, src }, i) => {
				if (i == index) {
					return (
						(
							<img key={src} alt={alt} className='img' src={src} width="100%" />
						)
					)
					
					return null
				}
			})}
			</div>
			{/* <img
				className="img"
				src={"https://picsum.photos/id/200/600/400"}
				width="100%"
			/> */}
			<br />
			<div className="prev-btn" onClick={handlePrev}>
				&#x21fd;
			</div>
			<div className="next-btn" onClick={handleNext}>
				&#x21fe;
			</div>
			{/* <div> */}

			<div className="indicators">
				{images.map((_, i) => {
					if (i == index) {
						return (
						<div className="circle circle-active"></div>
					)
					}
					return (
						<div className="circle"></div>
					)
				})}
			</div>
				{/* </div> */}
		</div>
	);
}
