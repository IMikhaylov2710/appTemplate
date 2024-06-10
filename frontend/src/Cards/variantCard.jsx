import './variantCard.css'

function VarCard(props) {
    return <div className={props.exonic ? "redBorder" : "greenBorder"}>
        <div className="header"><h1>chr{props.chromosome}:</h1><h2>{props.position.toString()}</h2></div>
        <div className="gene">Gene: {props.gene}</div>
        <div className="consequence">Consequence: {props.consequence}</div>
        <div className='depth>'>Depth: {props.depth}</div>
    </div>
}

export {VarCard}
