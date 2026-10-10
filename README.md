# Black Hole Gravitational Lensing: A Mini Simulation

A small Python project exploring how a compact object's gravitational field can bend light. It is a portfolio starter connecting computational mathematics with my interests in black hole physics, gravitational lensing, and numerical visualization.

## Research interests
- Black hole shadows and gravitational lensing
- Applied and computational mathematics
- Numerical modelling and scientific visualization
- Theoretical physics and relativistic astrophysics

## What this project does
- Implements a simple weak-field light-deflection approximation
- Plots deflection angle against impact parameter
- Keeps the model and its assumptions explicit

> **Important:** This is an illustrative weak-field approximation, not a full general-relativistic ray-tracing model and not a reproduction of either of my papers.

## Model
In units where \(G=c=1\), the leading-order weak-field deflection is

\[
\alpha \approx \frac{4M}{b},
\]

where \(M\) is the lens mass and \(b\) is the impact parameter. The approximation is most appropriate when the impact parameter is much larger than the gravitational radius.

## Run it
```bash
python -m pip install -r requirements.txt
python src/lensing_demo.py
```

The script saves `outputs/deflection_vs_impact_parameter.png`.

## Tools
Python, NumPy, Matplotlib

## About me
I am interested in applied mathematics, computational modelling, and theoretical physics, including black hole stability and gravitational lensing. This repository is a small educational project and a starting point for more advanced numerical work.

For my publications and academic background, see my [CV](#) or visit my GitHub profile: `github.com/nailaaslam2003`.

## Possible next steps
- Compare the weak-field approximation with numerical geodesic integration
- Explore how lens mass changes the deflection curve
- Extend the model toward photon-sphere and black-hole-shadow calculations
