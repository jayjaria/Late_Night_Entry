export default function Card(props) {
  return (
    <div className="card">
      {!props.headerNotRequired && (
        <div class="card-header">
          <img
            src={process.env.PUBLIC_URL + "/IIITG_Logo.jpg"}
            alt="Logo of IIITG"
          />
        </div>
      )}
      <div className="card-body">{props.children}</div>
    </div>
  );
}
