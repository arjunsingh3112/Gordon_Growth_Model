# Gordon_Growth_Model
A simple Python project that looks at stock valuation using the Gordon Growth Model (Dividend Discount Model) using TCS as Case Study.

I used TCS (Tata Consultancy Services) company as an example and visualized how estimated intrinsic value changes under different assumptions (values) for:

 *Required rate of return (r)
 
 *Dividend growth rate (g)

The goal is not really to predict a correct stock price, but to show how sensitive valuations are to these assumptions.

#Background Theory

The Gordon Growth Model values a stock as the present value of an infinite stream of growing dividends.

Formula:

P = D1 / (r - g)

Where:

 *P = Intrinsic value of the stock
 
 *D1 = Expected dividend next year
 
 *r = Required rate of return
 
 *g = Perpetual dividend growth rate

The model assumes:

 *Dividends grow at a constant rate forever
 
 *r > g
 
 *The company is mature and dividend-paying

In this analysis I used:

 *Stock: TCS
 
 *Annual dividend: ₹64 per share (excluding special dividends)
 
 *Current market price: ₹2161 per share (as on 13/06/26)

Growth rates tested: 4%, 5%, 6%, 7%, 8%, 9%

Required returns tested: 8%, 9%, 10%

#Some Observations from the visualisation: 
 
 *Small changes in growth assumptions can produce large changes in valuation for the same company.
 
 *The model is highly sensitive when r and g are close together.

#Limitations of the model
 
 It is a very simplified valuation framework.

Some limitations include:
 
 *Assumes perpetual constant growth.
 
 *Does not account for business cycles.
 
 *Not suitable for companies that do not pay stable dividends.
 *Results are extremely sensitive to estimates of r and g.

