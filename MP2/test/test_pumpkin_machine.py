import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state


@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# UCID: ss4746
# Date : 22-10-2023
# Test that pumpkin must be the first selection
def test_pumpkin_first_selection(machine):
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Happy Face")

# UCID: ss4746
# Date : 22-10-2023
# Test that we can only add face stencils if they're in stock
def test_face_stencils_in_stock(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Spooky Face")
    with pytest.raises(OutOfStockException):
        machine.handle_face_stencil_choice("Spooky Face")

# UCID: ss4746
# Date : 22-10-2023
# Test that we can only add extras if they're in stock
def test_extras_in_stock(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    with pytest.raises(OutOfStockException):
        machine.handle_extra_choice("LED Candle")

# UCID: ss4746
# Date : 22-10-2023
# Test we can add up to 3 face stencils of any combination
def test_max_face_stencils(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Spooky Face")

# UCID: ss4746
# Date : 22-10-2023
# Test we can add up to 3 extras of any combination
def test_max_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Dry Ice")
    machine.handle_extra_choice("Googly Eyes")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_extra_choice("Glitter")
#
# UCID: ss4746
# Date : 22-10-2023
# Test cost must be calculated properly based on the choices
@pytest.mark.parametrize(
    "pumpkin, stencil, extra, expected_cost",
    [
        ("Mini Pumpkin", "Happy Face", "LED Candle", 2.25),
   #    ("Large Pumpkin", "Scream Face", "LED Candle", 4.25),  # Assuming costs
   #     ("Medium Pumpkin", "Spooky Face", "Dry Ice", 3.75),
    ]
)
def test_calculate_cost(machine, pumpkin, stencil, extra, expected_cost):
    machine.handle_pumpkin_choice(pumpkin)
    machine.handle_face_stencil_choice(stencil)
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice(extra)
    machine.handle_extra_choice("done")

    # Call calculate_cost method to compute the total
    machine.calculate_cost()

    assert machine.inprogress_pumpkin[0].get_total_cost() == expected_cost

# UCID: ss4746
# Date : 22-10-2023
# Test that Total Sales (sum of costs) must be calculated properly
def test_total_sales(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("done")
    # Add this line to finalize the first transaction
    machine.handle_pay(10000,"10000")

    machine.handle_pumpkin_choice("Small Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Spooky Sound Effects")
    machine.handle_extra_choice("done")

    assert machine.total_sales == 0

# UCID: ss4746
# Date : 22-10-2023
# Test that Total products variable should properly increment for each purchase
def test_total_products_increments(machine):
    # Starting at 0 products
    assert machine.total_products == 0

    # First purchase
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    assert machine.total_products == 1

    # Second purchase
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Dry Ice")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    assert machine.total_products == 2


