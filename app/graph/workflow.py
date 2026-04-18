from langgraph.graph import StateGraph
from typing import TypedDict, Optional

from app.services.pdf_loader import extract_pages
from app.services.segregator import classify_pages
from app.services.id_agent import extract_identity
from app.services.discharge_agent import extract_discharge
from app.services.bill_agent import extract_bill


# Define state
class GraphState(TypedDict, total=False):
    claim_id: str
    file: any
    pages: list
    classified: dict
    id_data: dict
    discharge_data: dict
    bill_data: dict
    result: dict


# Nodes
def id_node(state):
    classified = state.get("classified", {})
    pages = classified.get("identity_document", [])
    data = extract_identity(pages)
    return {"id_data": data}


def segregator_node(state):
    classified = classify_pages(state["pages"])
    return {"classified": classified}


def id_node(state):
    classified = state.get("classified", {})
    pages = classified.get("identity_document", [])
    data = extract_identity(pages)
    return {"id_data": data}


def discharge_node(state):
    classified = state.get("classified", {})
    pages = classified.get("discharge_summary", [])
    data = extract_discharge(pages)
    return {"discharge_data": data}


def bill_node(state):
    classified = state.get("classified", {})
    pages = classified.get("itemized_bill", [])
    data = extract_bill(pages)
    return {"bill_data": data}

def load_pdf(state):
    pages = extract_pages(state["file"])
    return {"pages": pages}


def aggregator_node(state):
    classified = state.get("classified", {})

    return {
        "result": {
            "claim_id": state.get("claim_id"),
            "classification": {
                key: len(value) for key, value in classified.items()
            },
            "identity_data": state.get("id_data", {}),
            "discharge_data": state.get("discharge_data", {}),
            "bill_data": state.get("bill_data", {})
        }
    }


# Build Graph
def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("load_pdf", load_pdf)
    graph.add_node("segregator", segregator_node)
    graph.add_node("id_agent", id_node)
    graph.add_node("discharge_agent", discharge_node)
    graph.add_node("bill_agent", bill_node)
    graph.add_node("aggregator", aggregator_node)

    graph.set_entry_point("load_pdf")

    graph.add_edge("load_pdf", "segregator")
    graph.add_edge("segregator", "id_agent")
    graph.add_edge("segregator", "discharge_agent")
    graph.add_edge("segregator", "bill_agent")

    graph.add_edge("id_agent", "aggregator")
    graph.add_edge("discharge_agent", "aggregator")
    graph.add_edge("bill_agent", "aggregator")

    graph.set_finish_point("aggregator")

    return graph.compile()