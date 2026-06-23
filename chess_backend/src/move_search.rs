//------------------------------------------------------------------------------
//MOVE SEARCH
//------------------------------------------------------------------------------

//move search is the file where the opponent algorithm searches for the best move
//to make out of all legal moves.

use crate::board_evaluation;
use crate::move_generation;
use crate::move_validation;

//------------------------------------------------------------------------------
//libaries
//------------------------------------------------------------------------------
use pyo3::prelude::*;
use pyo3::types::PyList;

//------------------------------------------------------------------------------
//move searching algorithm
//------------------------------------------------------------------------------
#[pymodule]
pub fn find_best_move(chess_board: &Pylist) {
    //just parameters for now
}