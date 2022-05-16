from dolfin import *
import matplotlib.pyplot as plt

# Create mesh and define function space
mesh = UnitSquareMesh(6, 4)
V = FunctionSpace(mesh, "Lagrange", 1)
# Define boundary conditions
u0 = Expression("1 + x[0]*x[0] + 2*x[1]*x[1]",degree=2)
def u0_boundary(x, on_boundary):
    return on_boundary
bc = DirichletBC(V, u0, u0_boundary)
# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(-6.0)
a = inner(nabla_grad(u), nabla_grad(v))*dx
L = f*v*dx
# Compute solution
u = Function(V)
solve(a == L, u, bc)
# Plot solution and mesh
plot(u)
plt.show()
plot(mesh)
plt.show()
# Dump solution to file in VTK format
file = File("poisson.pvd")
file << u


