#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # keep track of index of the route array
    routeStopIndex = 0
    route = ['NONE'] * length
    # use dictionary to keep track of source and destinations
    ticketDict = {ticket.source: ticket.destination for ticket in tickets}

    # set the start of the trip
    currticket = "NONE"
    # iterates until the destination of the current ticket is NONE
    while ticketDict[currticket] != 'NONE':
        # assign the place in the route array to the destination of the current ticket
        route[routeStopIndex] = ticketDict[currticket]
        # increment the route stop index
        routeStopIndex += 1
        # set the current ticket to the destination of the ticket we just added to the route
        currticket = ticketDict[currticket]

    return route
