//------------------------------------------------------------------------------
//BOARD EVALUATION
//------------------------------------------------------------------------------

//This is where the algorithm evaluates the board to calculate its score weighted
//towards one side (either white or black). basically shows the position of the game
//by giving the board a score.

//------------------------------------------------------------------------------
//libraries
//------------------------------------------------------------------------------
use pyo3::prelude::*;
use pyo3::types::PyList;

//------------------------------------------------------------------------------
//board evaluation function
//------------------------------------------------------------------------------
#[pymodule]
pub fn evaluate_board(chess_board: &Pylist) -> Pyresult<i32> {
    score = 0 //placeholder value for now
}