//------------------------------------------------------------------------------
//MOVE VALIDATION
//------------------------------------------------------------------------------

//the main file where I write my move validation for the player and the algorithm
//so that they both only make legal moves.

//------------------------------------------------------------------------------
//other files
//------------------------------------------------------------------------------
use crate::move_generation;

//------------------------------------------------------------------------------
//libraries
//------------------------------------------------------------------------------
use pyo3::prelude::*;
use pyo3::types::{PyList};

//------------------------------------------------------------------------------
//move validation function
//------------------------------------------------------------------------------
#[pymodule]
pub fn validate_move(chess_board: &PyList, starting_row: usize, starting_column: usize, ending_row: usize, ending_column: usize) -> PyResult<bool> {

    //just parameters for now
}