//------------------------------------------------------------------------------
// main lib file for the rust chess backend
------------------------------------------------------------------------------
use pyo3::prelude::*;

#[pymodule]
fn chess_backend(_py: Python, _m: &PyModule) -> PyResult<()> {
    Ok(())
}
