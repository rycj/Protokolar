import aspose
from aspose import words as aw
from aspose import CreateOrUpdateDocumentRequest
from aspose import InsertMathObjectRequest
from aspose.words.fields import FieldEQ


doc = aw.Document()
builder = aw.DocumentBuilder(doc)

# An EQ field displays a mathematical equation consisting of one or many elements.
# Each element takes the following form: [switch][options][arguments].
# There may be one switch, and several possible options.
# The arguments are a set of coma-separated values enclosed by round braces.

# Here we use a document builder to insert an EQ field, with an "\f" switch, which corresponds to "Fraction".
# We will pass values 1 and 4 as arguments, and we will not use any options.
# This field will display a fraction with 1 as the numerator and 4 as the denominator.
field = ExField.insert_field_eq(builder, r"\f(1,4)")

self.assertEqual(r" EQ \f(1,4)", field.get_field_code())

# One EQ field may contain multiple elements placed sequentially.
# We can also nest elements inside one another by placing the inner elements
# inside the argument brackets of outer elements.
# We can find the full list of switches, along with their uses here:
# https://blogs.msdn.microsoft.com/murrays/2018/01/23/microsoft-word-eq-field/

# Below are applications of nine different EQ field switches that we can use to create different kinds of objects.
# 1 -  Array switch "\a", aligned left, 2 columns, 3 points of horizontal and vertical spacing:
ExField.insert_field_eq(builder, r"\a \al \co2 \vs3 \hs3(4x,- 4y,-4x,+ y)")

# 2 -  Bracket switch "\b", bracket character "[", to enclose the contents in a set of square braces:
# Note that we are nesting an array inside the brackets, which will altogether look like a matrix in the output.
ExField.insert_field_eq(builder, r"\b \bc\[ (\a \al \co3 \vs3 \hs3(1,0,0,0,1,0,0,0,1))")

# 3 -  Displacement switch "\d", displacing text "B" 30 spaces to the right of "A", displaying the gap as an underline:
ExField.insert_field_eq(builder, r"A \d \fo30 \li() B")

# 4 -  Formula consisting of multiple fractions:
ExField.insert_field_eq(builder, r"\f(d,dx)(u + v) = \f(du,dx) + \f(dv,dx)")

# 5 -  Integral switch "\i", with a summation symbol:
ExField.insert_field_eq(builder, r"\i \su(n=1,5,n)")

# 6 -  List switch "\l":
ExField.insert_field_eq(builder, r"\l(1,1,2,3,n,8,13)")

# 7 -  Radical switch "\r", displaying a cubed root of x:
ExField.insert_field_eq(builder, r"\r (3,x)")

# 8 -  Subscript/superscript switch "/s", first as a superscript and then as a subscript:
ExField.insert_field_eq(builder, r"\s \up8(Superscript) Text \s \do8(Subscript)")

# 9 -  Box switch "\x", with lines at the top, bottom, left and right of the input:
ExField.insert_field_eq(builder, r"\x \to \bo \le \ri(5)")

# Some more complex combinations.
ExField.insert_field_eq(
    builder,
    r"\a \ac \vs1 \co1(lim,n→∞) \b (\f(n,n2 + 12) + \f(n,n2 + 22) + ... + \f(n,n2 + n2))",
)
ExField.insert_field_eq(builder, r"\i (,,  \b(\f(x,x2 + 3x + 2))) \s \up10(2)")
ExField.insert_field_eq(
    builder, r"\i \in( tan x, \s \up2(sec x), \b(\r(3) )\s \up4(t) \s \up7(2)  dt)"
)

doc.save(ARTIFACTS_DIR + "Field.field_eq.docx")


@staticmethod
def insert_field_eq(builder: aw.DocumentBuilder, args: str) -> aw.fields.FieldEQ:
    """Use a document builder to insert an EQ field, set its arguments and start a new paragraph."""

    field = builder.insert_field(aw.fields.FieldType.FIELD_EQUATION, True).as_field_eq()
    builder.move_to(field.separator)
    builder.write(args)
    builder.move_to(field.start.parent_node)

    builder.insert_paragraph()
    return field
