// import { useState } from 'react';

import { useEffect, useState } from "react";

// // List of cell indices that are 3-in-a-row.
// const CELLS_IN_A_LINE = [
//   [0, 1, 2],
//   [3, 4, 5],
//   [6, 7, 8],
//   [0, 3, 6],
//   [1, 4, 7],
//   [2, 5, 8],
//   [0, 4, 8],
//   [2, 4, 6],
// ];

// // Determine if there's a winner for the board.
// function determineWinner(board) {
//   for (let i = 0; i < CELLS_IN_A_LINE.length; i++) {
//     const [x, y, z] = CELLS_IN_A_LINE[i];
//     // Determine if the cells in a line have the same mark.
//     if (
//       board[x] != null &&
//       board[x] === board[y] &&
//       board[y] === board[z]
//     ) {
//       return board[x];
//     }
//   }

//   // No winner yet.
//   return null;
// }

// function Cell({ index, disabled, mark, turn, onClick }) {
//   return (
//     <button
//       aria-label={
//         mark == null
//           ? `Mark cell ${index} as ${turn}`
//           : undefined
//       }
//       className="cell"
//       disabled={disabled}
//       onClick={onClick}>
//       <span aria-hidden={true}>{mark}</span>
//     </button>
//   );
// }

// export default function TicTacToe() {
//   const [board, setBoard] = useState(Array(9).fill(null));
//   const [xIsPlaying, setIsXPlaying] = useState(true);

//   const winner = determineWinner(board);

//   function onReset() {
//     setBoard(Array(9).fill(null));
//     setIsXPlaying(true);
//   }

//   function getStatusMessage() {
//     if (winner != null) {
//       return `Player ${winner} wins!`;
//     }

//     // All cells have been filled up.
//     if (!board.includes(null)) {
//       return `It's a draw!`;
//     }

//     return `Player ${xIsPlaying ? 'X' : 'O'} turn`;
//   }

//   return (
//     <div className="app">
//       <div aria-live="polite">{getStatusMessage()}</div>
//       <div className="board">
//         {Array(9)
//           .fill(null)
//           .map((_, index) => index)
//           .map((cellIndex) => {
//             const turn = xIsPlaying ? 'X' : 'O';
//             return (
//               <Cell
//                 key={cellIndex}
//                 disabled={
//                   board[cellIndex] != null || winner != null
//                 }
//                 index={cellIndex}
//                 mark={board[cellIndex]}
//                 turn={turn}
//                 onClick={() => {
//                   const newBoard = board.slice();
//                   newBoard[cellIndex] = turn;
//                   setBoard(newBoard);
//                   setIsXPlaying(!xIsPlaying);
//                 }}
//               />
//             );
//           })}
//       </div>
//       <button
//         onClick={() => {
//           if (winner == null) {
//             // Confirm whether to reset the game.
//             const confirm = window.confirm(
//               'Are you sure you want to reset the game?',
//             );
//             if (!confirm) {
//               return;
//             }
//           }

//           onReset();
//         }}>
//         Reset
//       </button>
//     </div>
//   );
// }

const DIAG1 = [[0,0], [1,1], [2,2]]
const DIAG2 = [[2,0], [1,1], [0,2]]

export default function TicTacToe({ n }) {
	const [grid, setGrid] = useState(
		Array.from({ length: n }, () => Array(n).fill(0))
	);

	const [winner, setWinner] = useState(null)


	const [isXTurn, setIsXTurn] = useState(true);
	// console.log(grid);

	const updateGrid = (r, c) => {
		const value = isXTurn ? 1 : -1;
		const copy = grid.map((row) => row.slice());
		copy[r][c] = value;
		setGrid(copy);
		setIsXTurn(!isXTurn);
		determineWinner(copy, r, c)
	};

	const determineWinner = (updatedGrid, r, c) => {
		const row = updatedGrid[r]
		const col = []
		for (let i = 0; i < n; i++) {
			col.push(updatedGrid[i][c])
		}
		const diag1 = []
		for (const [x, y] of DIAG1) {
			diag1.push(updatedGrid[x][y])
		}

		const diag2 = []
		for (const [x, y] of DIAG2) {
			diag2.push(updatedGrid[x][y])
		}

		[row, col, diag1, diag2].forEach(el => {
			const sum = el.reduce((acc, cur) => acc + cur, 0)
			console.log('sum', sum)
			if (sum === 3) {
				setWinner('X')
				return
			}

			if (sum === -3) {
				setWinner('O')
				return
			}
		})
	}

	const reset = () => {
		const resetBoard = Array.from({ length: n }, () => Array(n).fill(0));
		setGrid(resetBoard);
		setIsXTurn(true);
		setWinner(null)
	};


	const getStatusMessage = () => {
		if (winner === 'X') {
			return 'X is the winner'
		}
		if (winner === 'O') {
			return 'O is the winner'
		}

		// check draw
		const hasEmpty = grid.some(row => row.includes(0))
		if (!hasEmpty) {
			return "It's a draw"
		}


		// check turn
		if (isXTurn) {
			return 'X turn'
		} else {
			return 'O turn'
		}

	}

	return (
		<div className="game">
			<div className="head">{getStatusMessage()}</div>
			
			<div className="board">
				{grid.map((row, r) => {
					return (
						<div className="row">
							{row.map((col, c) => {
								return (
									<button
										disabled={grid[r][c] || winner}
										onClick={() => updateGrid(r, c)}
										className="cell"
									>
										{grid[r][c] === 1 ? 'X' : grid[r][c] === -1 ? 'O' : ''}
									</button>
								);
							})}
						</div>
					);
				})}
			</div>

			<div>
				<button onClick={reset}>Reset</button>
			</div>
		</div>
	);
}
