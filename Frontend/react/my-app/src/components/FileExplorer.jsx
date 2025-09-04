import React from 'react'
import { useState } from 'react'

export default function FileExplorer({ data, layer = 0 }) {
	const [expand, setExpand] = useState({})

	const handleExpand = (id) => {
		console.log('id', id)
		setExpand(prev => {
			return {
				...prev,
				[id]: !prev[id]
			}
		})
	}

	return (
		<div>{data.map(d => {
			if (d.children) {
				// this is a folder
				return (
					<>
						<div key={d.id} style={{
							marginLeft: `${layer * 20}px`
						}}>
							<b>{d.name} </b>
							<span onClick={() => handleExpand(d.id)} style={{ cursor: 'pointer' }}>[{expand[d.id] ? '-' : '+'}]</span>
						</div>
						{/* render childern based on expand state */}
						<div style={{
							display: expand[d.id] ? 'block': 'none'
						}}>
							{FileExplorer({
							data: d.children,
							layer: layer + 1
						})}
						</div>
					</>
				)
			} else {
				//   this is a file
				return <div key={d.id} style={{
					marginLeft: `${layer * 20}px`
				}}>
					{d.name}
				</div>
			}
		})}</div>
	)
}
