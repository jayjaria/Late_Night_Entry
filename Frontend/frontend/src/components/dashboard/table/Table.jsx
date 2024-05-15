export default function Table({ data = [], columns = [] }) {
  return (
    <table className="table table-striped table-hover">
      <thead>
        <tr>
          {columns.map((column, index) => (
            <th key={index}>{column}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((log, index) => (
          <tr key={index}>
            <td>{log.rollNo}</td>
            <td>{log.studentName}</td>
            <td>{log.createdBy}</td>
            <td>{log.createdAt}</td>
            <td></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
